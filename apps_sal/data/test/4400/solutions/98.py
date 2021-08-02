s = input()
print((3 if s == 'RRR' else 2 if s == 'RRS' or s == 'SRR'
       else 1 if s == 'RSS' or s == 'SRS' or s == 'RSR' or s == 'SSR' else 0))
