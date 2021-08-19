# https://codeforces.com/contest/1288/problem/B

def main():
    a, b = list(map(int, input().split()))
    ans = a * (len(str(b + 1)) - 1)
    print(ans)


t = int(input())
for i in range(t):
    main()
