s = input()
ans = [i for (index, i) in enumerate(s, start=1) if index % 2 != 0]
print(''.join(ans))
