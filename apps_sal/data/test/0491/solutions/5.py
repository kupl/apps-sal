n = int(input())
count1 = n
count2 = int(float(n) / 10)
count3 = n
count3 = str(count3)
count4 = count3[0:-2]
count4 += count3[-1]
count4 = int(count4)
print(max(count4, count1, count2))
