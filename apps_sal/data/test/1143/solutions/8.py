
fin = open("input.txt", "r")
fout = open("output.txt", "w")

mon = [0,31,28,31,30,31,30,31,31,30,31,30,31]
ans = [0]*500
ba = []
for i in range(int(fin.readline())):
   m,d,p,t = map(int,fin.readline().split())
   ba.append([m,d,p,t])

for i in ba:
    days = sum(mon[:i[0]]) + i[1] + 100
    for j in range(1,i[3]+1):
        ans[days - j]+=i[2]

print(max(ans), file=fout)





