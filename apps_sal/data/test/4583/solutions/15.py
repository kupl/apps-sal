import itertools

ads = ["+","+","+","-","-","-"]
s = input()
q = list(itertools.permutations(ads, 3))

for j in range(len(q)):
    ans = int(s[0])
    al = ""
    for k in range(3):
        if q[j][k] == "+":
            ans += int(s[k+1])
        else:
            ans -= int(s[k+1])
        al += q[j][k]
        al += s[k+1]
    if ans == 7:
        print(s[0]+al+"=7")
        break
