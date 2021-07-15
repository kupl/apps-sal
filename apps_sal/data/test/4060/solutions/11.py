input()
line = input()
wasm = -1
last0 = 0
last1 = -1
curs = 0
err = False
for i in range(len(line)):
    if line[i]=='(':
        curs+=1
    else:
        curs-=1
    if curs == 0:
        last0=i
    if curs == 1:
        last1=i
    if curs < 0:
        if wasm == -1:
            wasm=i
        if curs < -2:
            err = True
            break
if err:
    print(0)
elif wasm == -1:
    if curs != 2:
        print(0)
    else:
        print(int((len(line)-max(last0,last1))/2))
else:
    if curs != -2:
        print(0)
    else:
        print(int(wasm/2) + 1)
