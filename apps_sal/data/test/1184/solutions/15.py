s = input()

if s == '{}':
    print(0)
else:
    print(len(set(s.strip('}{').split(', '))))
