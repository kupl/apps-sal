ss = input()
if ss[0] == ss[-1] and len(ss) % 2 == 0 or (ss[0] != ss[-1] and len(ss) % 2):
    print('First')
else:
    print('Second')
