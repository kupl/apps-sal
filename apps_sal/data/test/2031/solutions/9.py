n = int(input())
a = list(map(int, input().split()))
m = int(input())
for i in range(m):
    k, pos = map(int, input().split())
    save = []
    for j in range(len(a)):
        save.append(a[j])
    ans = []
    for x in range(k):
        maximum = 0
        pr = -1
        for j in range(len(save)):
            if save[j] > maximum:
                maximum = save[j]
                pr = j
        ans.append(maximum)
        save.pop(pr)
    ans.sort()
    answer = []
    for i in range(len(a)):
        if a[i] in ans:
            answer.append(a[i])
            ans.pop(ans.index(a[i]))
    print(answer[pos - 1])
