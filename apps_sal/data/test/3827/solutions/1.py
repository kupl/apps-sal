a = input()
if a.count('a') == a.find('b') and a.count('a') + a.count('b') == a.find('c') and (a.count('a') == a.count('c') or a.count('b') == a.count('c')) and a.count('a') * a.count('b'):
    print("YES")
else:
    print("NO")
