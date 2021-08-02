n = int(input())
p = input().split(" ")
for i in range(len(p)):
    p[i] = int(p[i])
ans = []
for i in range(len(p)):
    scores = [0 for _ in range(n)]
    max_score = 0
    curr = i
    while True:
        #print(scores, curr)
        scores[curr] += 1
        if scores[curr] == 2:
            ans.append(curr + 1)
            break
        curr = p[curr] - 1
s = ""
for i in range(len(ans)):
    if i != len(ans) - 1:
        s += str(ans[i]) + " "
    else:
        s += str(ans[i])
print(s)
