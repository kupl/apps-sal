s = input()
k = int(input())
w = list(map(int, input().split(' ')))

sum = 0

for index, el in enumerate(s):
    sum += w[ord(el)-97] * (index+1)
 
max_w = max(w);
result = max_w * (((len(s)+1) + (len(s)+k))/2) * k
print(int(sum + result))
