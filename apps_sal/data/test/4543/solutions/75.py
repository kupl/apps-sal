ab = int(input().replace(' ', ''))
ans = False
for i in range(320):
    if i * i == ab:
        ans = True
        break
print('Yes') if ans else print('No')
