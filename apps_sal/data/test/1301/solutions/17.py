n = int(input())
w = input()
l = ['vaporeon', 'jolteon', 'flareon', 'espeon', 'umbreon', 'leafeon', 'glaceon'
     ,'sylveon']
for i in l:
    if len(w) == len(i):
        p = ''
        j = 0
        while j < len(w):
            if w[j] == '.':
                p += i[j]
            elif w[j] == i[j]:
                p += i[j]
            else:
                break
            j += 1
        if p in l:
            print(p)
            break
       
            
    

