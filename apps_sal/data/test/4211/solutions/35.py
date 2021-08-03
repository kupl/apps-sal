n = int(input())
B = list(map(int, input().split()))
ans = [B[0]]
for i in range(len(B)):
    if i != len(B) - 1:
        if B[i] > B[i + 1]:
            ans.append(B[i + 1])
        else:
            ans.append(B[i])
    else:
        ans.append(B[i])
print(sum(ans))
