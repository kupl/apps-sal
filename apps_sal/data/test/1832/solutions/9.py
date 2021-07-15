alphabet = "qwertyuiopasdfghjklzxcvbnm"


def solve():
    n = int(input())
    a = list(map(int, input().split()))
    last = "a" * 51
    print(last)
    for i in range(n):
        last = last[:a[i]] + alphabet[alphabet.index(last[a[i]]) - 1] + "a" * 50
        print(last)


for _ in range(int(input())):
    solve()

