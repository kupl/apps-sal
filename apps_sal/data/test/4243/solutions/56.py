N = int(input())
happy = 0
if(N >= 500):
  happy = happy +  (int(N/500)*1000)
  N = N%500
if(N>=5):
  happy = happy + (int(N/5)*5)
  N = N%5
print(happy)
