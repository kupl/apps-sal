M, K = list(map(int, input().split()))

if M <= 1:
    if K > 0:
        print(-1)
        return
    else:
        if M == 1:
            print(" ".join(["0", "0", "1", "1"]))
            return
        else:
            print("0 0")
            return
elif K >= 2 ** M:
    print(-1)
    return
ans = [str(K)]
exclude_k = [str(i) for i in range(2 ** M) if i != K]
ans.extend(exclude_k)
ans.append(str(K))
ans.extend(exclude_k[::-1])
print(" ".join(ans))
