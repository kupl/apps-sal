import os
import sys
from io import BytesIO, IOBase


def main():
    pass


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


def binary(n):
    return (bin(n).replace("0b", ""))


def decimal(s):
    return (int(s, 2))


def pow2(n):
    p = 0
    while (n > 1):
        n //= 2
        p += 1
    return (p)


def isPrime(n):
    if (n == 1):
        return (False)
    else:
        root = int(n ** 0.5)
        root += 1
        for i in range(2, root):
            if (n % i == 0):
                return (False)
        return (True)


s = input()
f = [0] * 10
mod = [1869, 8961, 6981, 6198, 1698, 9861, 1896]
for i in s:
    f[int(i)] += 1
a = ""
cm = 0
for i in s:
    if(i != "0"):
        n = int(i)
        if(n == 1 or n == 6 or n == 8 or n == 9):
            if(f[n] > 1):
                cm = (cm * 10 + n) % 7
                f[n] -= 1
                print(i, end="")
        else:
            cm = (cm * 10 + n) % 7
            f[n] -= 1
            print(i, end="")
for i in range(0, 4):
    cm = (cm * 10) % 7
if(cm == 0):
    print(str(mod[cm]), end="")
    print('0' * f[0])
else:
    print(str(mod[7 - cm]), end="")
    print('0' * f[0])
