N = int(input())
S = input()

x = 0
lst = [0]

for i in range(N):
   if S[i] == 'I':
      x += 1
   else:
      x -= 1
   lst.append(x)

print(max(lst))
