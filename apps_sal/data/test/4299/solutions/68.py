d = {n: 'hon' for n in '24579'}
d.update({n: 'pon' for n in '0168'})
d.update({'3': 'bon'})
print(d[input()[-1]])
