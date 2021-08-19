S = input()
ans = -S[::-1].find('Z') - S.find('A') + len(S)
print(ans)
