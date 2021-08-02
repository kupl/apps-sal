N = int(input())

data = [input() for _ in range(N)]


def f(s):
    c = len([x for x in data if x in s])
    print(f"{s} x {c}")


f("AC")
f("WA")
f("TLE")
f("RE")
