p = input()

if 'b' <= p[0] <= 'g' and '2' <= p[1] <= '7':
    print(8)
elif p in ['a1', 'a8', 'h1', 'h8']:
    print(3)
else:
    print(5)
