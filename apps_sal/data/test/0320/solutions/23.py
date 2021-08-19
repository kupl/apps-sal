import sys


class Reader:

    def __init__(self, file):
        (self.tok, self.tok_length, self.tok_position) = ([], 0, 0)
        (self.lines, self.line_position) = (file.readlines(), 0)

    def next_token(self):
        if self.tok_position < self.tok_length:
            self.tok_position += 1
            return self.tok[self.tok_position - 1]
        self.tok = self.lines[self.line_position].split()
        (self.tok_length, self.tok_position) = (len(self.tok), 0)
        self.line_position += 1
        return self.next_token()

    def next_line(self):
        (self.tok, self.tok_length, self.tok_position) = ([], 0, 0)
        self.line_position += 1
        return self.lines[self.line_position - 1]


def main():
    reader = Reader(sys.stdin)
    n = int(reader.next_token())
    ls = 0
    rs = 0
    cnt = 0
    for i in range(n):
        l = int(reader.next_token())
        r = int(reader.next_token())
        ls += l
        rs += r
        if l % 2 != r % 2:
            cnt += 1
    if (ls + rs) % 2 != 0:
        print(-1)
        return
    if ls % 2 == 0 and rs % 2 == 0:
        print(0)
        return
    if cnt > 0:
        print(1)
        return
    print(-1)


def __starting_point():
    main()


__starting_point()
