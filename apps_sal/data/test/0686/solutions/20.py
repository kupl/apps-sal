q = int(input())
for query in range(q):
    m, n = list(map(int, input().split()))
    if m - n <= 1:
        print("NO")
    else:
        print("YES")
# n = int(input())
# l = map(int, input().split())
# impossible = False
# res = 0

# for i in range(len(i)):

# if not impossible:
#   print(res)
# else:
#   print("-1")
