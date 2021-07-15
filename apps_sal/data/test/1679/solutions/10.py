n = int(input())
s = input()
curr = 0

for char in s:
    if char == '1':
        curr += 1
    else:
        print(curr, end = '')
        curr = 0
        
print(curr)

