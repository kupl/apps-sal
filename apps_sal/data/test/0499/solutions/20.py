n = int(input())
s = input()
d = {}
(B, G, R) = (s.count('B'), s.count('G'), s.count('R'))
if B == 0 and G == 0:
    print('R')
elif B == 0 and R == 0:
    print('G')
elif G == 0 and R == 0:
    print('B')
elif B == 0 and G == 1 and (R == 1):
    print('B')
elif B == 1 and G == 0 and (R == 1):
    print('G')
elif B == 1 and G == 1 and (R == 0):
    print('R')
elif B == 0 and G == 1:
    print('BG')
elif B == 0 and R == 1:
    print('BR')
elif G == 0 and B == 1:
    print('BG')
elif G == 0 and R == 1:
    print('GR')
elif R == 0 and B == 1:
    print('BR')
elif R == 0 and G == 1:
    print('GR')
else:
    print('BGR')
