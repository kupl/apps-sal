luv = input()
cf = input()
onegod = 0
zerogod = 0
for I in cf:
    if I == '1':

        onegod += 1

zerogod = len(cf) - onegod
print(abs(onegod - zerogod))
