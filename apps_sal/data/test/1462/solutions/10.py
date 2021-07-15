n,k = list(map(int, input().split()))
s = input()
ch = []
re = {}
limit = len(s)
c = 1
for i in range(limit):
    #print(s[i])
    if s[i] in re :
        re[s[i]] += 1
    else:
        re[s[i]] = 1
        ch.append(s[i])
li = len(ch)
score = []
for i in range(li):
    score.append(re[ch[i]])
score.sort(reverse = True)
#print(score)
last = len(score)
out = 0
for i in range(last):
    if k == 0 :
        break
    if k == score[i]:
        out  += score[i] * score[i]
        break
    elif k > score[i] :
        out += score[i] * score[i]
        k -= score[i]
    elif k < score[i]:
        out += k * k
        break
   # print(out)
print(out)
    

