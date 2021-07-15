a=input()
a=" ".join(a)
a=a.split()
suma=0
contador=0
for k in range (len(a)):
        if a[k]!="*":
                igual=a[k]
                contador=0
                for r in range (k+1,len(a)):
                        if a[k]==a[r]:
                                contador=contador+1
                                a[r]="*"
                        else:
                                break
                if contador%2!=0:
                        suma=suma+1
print(suma)
