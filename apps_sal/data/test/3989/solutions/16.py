
import os
import sys
from io import BytesIO, IOBase


def main():
    x = input().strip()
    ls = []
    fl = [0, 0, 0, 0]
    st = '1689'
    for i in x:
        if i in st and not fl[st.index(i)]:
            fl[st.index(i)] = 1
            continue
        ls.append(i)
    ls1 = ls[::-1]
    perm = ['1869', '1968', '1689', '6198', '1698', '1986', '1896']
    val = [1, 3, 2, 6, 4, 5]
    rem = 0
    for i in range(len(ls1)):
        rem += (int(ls1[i]) * val[i % 6]) % 7
        rem %= 7
    ls = list(perm[((7 - rem) * pow(pow(10, len(ls1), 7), 5, 7)) % 7]) + ls
    print(''.join(ls))


BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
def input(): return sys.stdin.readline().rstrip("\r\n")


def __starting_point():
    main()


__starting_point()
