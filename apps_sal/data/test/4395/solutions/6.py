n = int(input())

s = input()

G = ['GRB','GBR','RBG','RGB','BGR','BRG']

best = 10**10
guy = None

for i in G:
    temp = 0
    for j in range(n):
        if s[j] != i[j%3]:
            temp += 1
    if temp < best:
        best = temp
        guy = i

print(best)
print(guy*(n//3)+guy[:n%3])


