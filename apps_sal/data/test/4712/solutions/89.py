H, W = list(map(int, input().split()))
A = [list(input()) for _ in range(H)]

# 一段目
print(("#"*(W+2)))
for a in A:
    print(("#" + "".join(a) + "#"))
# 最終段
print(("#"*(W+2)))

