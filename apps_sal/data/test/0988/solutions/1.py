table = [[3, 3, 0, 4, 4, 0, 3, 3],
         [3, 3, 0, 4, 4, 0, 3, 3],
         [2, 2, 0, 3, 3, 0, 2, 2],
         [2, 2, 0, 3, 3, 0, 2, 2],
         [1, 1, 0, 2, 2, 0, 1, 1],
         [1, 1, 0, 2, 2, 0, 1, 1]]



l = []
for i in range(6):
    s = input();
    ll = [] 
    for c in s:
        ll.append(c)
    l.append(ll)    

for k in [4, 3, 2, 1]:
    for i in range(6):
        for j in range(8):
            if (table[i][j] == k and l[i][j] == "."):
                l[i][j] = 'P';
                for ll in l:
                    s = ""
                    for c in ll:
                        s = s + c 
                    print(s)                
                return
