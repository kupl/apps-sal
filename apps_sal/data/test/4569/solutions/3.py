S=input()
a=['Sunny','Cloudy','Rainy']
for i in range(3):
    if a[i]==S:
        print((a[(i+1)%3]))

