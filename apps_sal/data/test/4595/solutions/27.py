s = input()

first = s.index('A')
end = s.rindex('Z')

ans = end - first + 1
print(ans)
