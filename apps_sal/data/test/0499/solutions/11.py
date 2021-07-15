n = int(input())
s = input()
st = {'R', 'G', 'B'}
if s.count(s[0]) == n:
    print(s[0])
elif st == set(s):
    print(''.join(sorted(list(st))))
elif len(set(s)) == 2:
    if s.count(list(set(s))[0]) > 1 and s.count(list(set(s))[1]) > 1:
        print(''.join(sorted(list(st))))
    elif s.count(list(set(s))[0]) > 1:
        print(''.join(sorted(list(st - set(s))[0] + list(set(s))[1])))
    elif s.count(list(set(s))[1]) > 1:
        print(''.join(sorted(list(st - set(s))[0] + list(set(s))[0])))
    else:
        print(list(st - set(s))[0])
