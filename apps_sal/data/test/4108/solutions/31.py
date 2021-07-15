S = input()
T = input()

alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

S_counter = []
T_counter = []
for i in alph:
    S_counter.append(S.count(i))
    T_counter.append(T.count(i))

S_counter.sort()
T_counter.sort()

if S_counter == T_counter:
    print('Yes')
else:
    print('No')

