# ABC109
# B Shiritori
N = int(input())
W = [input() for _ in range(N)]
if len(W) != len(set(W)):
    print("No")
    return
else:
    for i in range(N-1):
        if W[i][-1] != W[i+1][0]:
            print("No")
            return
pass
print("Yes")

