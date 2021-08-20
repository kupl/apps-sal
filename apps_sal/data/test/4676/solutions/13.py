O = list(input())
E = list(input())
ans = [0] * (len(O) + len(E))
for i in range(len(ans)):
    if i % 2 == 0:
        ans[i] = O[0]
        del O[0]
    else:
        ans[i] = E[0]
        del E[0]
print(''.join(ans))
