# init
t, a = input(), input()

t, a = t.replace('5', '2'), a.replace('5', '2')
t, a = t.replace('9', '6'), a.replace('9', '6')

ac = dict().fromkeys([i for i in a], 0)
for i in a:
    ac[i] += 1

print(min([ac[i] // t.count(i) for i in t]))
