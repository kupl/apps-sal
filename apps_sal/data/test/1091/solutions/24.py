# Made By Mostafa_Khaled
bot = True
n = int(input())

p = list(map(int, input().split()))

ll = p.index(max(p))

p.pop(ll)

print(ll + 1, max(p))

# Made By Mostafa_Khaled
