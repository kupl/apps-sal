s = input()
l = list(s)
cul = list(0 for i in range(30))
for el in l :
        cul[ord(el) - 97] += 1
if cul[ord('n')-97] > 0:
        cul[ord('n')-97]-=1


print(min(cul[ord('n')-97]//2 , min(cul[ord('e')-97]//3 , min(cul[ord('t')-97] , cul[ord('i')-97]))))

