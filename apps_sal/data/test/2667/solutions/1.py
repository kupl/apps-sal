n = int(input())
# s = n*(n+1)/2

stamps = list(map(int, input().split()))
# print(s)
# print(sum(stamps))
if (n*(n+1))/2 == sum(stamps):
    print("YES")
else:
    print("NO")
