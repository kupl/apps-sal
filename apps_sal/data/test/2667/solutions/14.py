# cook your dish here

n = int(input())
stamps = list(map(int, input().split()))
if n * (n + 1) / 2 == sum(stamps):
    print("YES")
else:
    print("NO")
