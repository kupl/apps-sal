arr = [int(i) for i in filter(None, input().split(" "))]
s = arr[0]
k = arr[1]
mx = arr[2]
arr = [int(i) for i in filter(None, input().split(" "))]
sum = 0
for i in range(k):
    sum += arr[i]
sum += (mx - 1) * (k + 1)
if sum < s:
    wer = "NO"
    print(wer)
else:
    wer = "YES"
    ans = [0] * (mx - 1)
    for i in range(k):
        ans += [i + 1] * arr[i]
        ans += [0] * (mx - 1)
    max = len(ans)
    for i in range(len(ans)):
        if max <= s:
            break
        else:
            if ans[i] == 0:
                ans[i] = -1
                max -= 1
    answer = []
    for i in range(len(ans)):
        if ans[i] != -1:
            answer.append(ans[i])
    print(wer)
    for i in range(len(answer)):
        print(answer[i], end=' ')
