import sys
sys.setrecursionlimit(10**9)


def mi(): return map(int, input().split())
def ii(): return int(input())
def isp(): return input().split()
def deb(text): print("-------\n{}\n-------".format(text))


INF = 10**20


class Counter:
    def __init__(self):
        self.dict = {}

    def add(self, x):
        if x in self.dict:
            self.dict[x] += 1
        else:
            self.dict[x] = 1

    def decrement(self, x):
        self.dict[x] -= 1
        if self.dict[x] <= 0:
            del self.dict[x]

    def get_dict(self):
        return self.dict


def main():
    S = input()
    counter = Counter()
    for s in S:
        counter.add(s)

    d = counter.get_dict()
    for s in ['a', 'b', 'c']:
        if not s in d or d[s] != 1:
            print("No")
            return

    print("Yes")


def __starting_point():
    main()


__starting_point()
