import math
A,B,H,M=list(map(int,input().split()))
Hx=math.cos(((H/12)+((1/12)*(M/60)))*2*math.pi)*A
Mx=math.cos((M/60)*2*math.pi)*B
Hy=math.sin(((H/12)+((1/12)*(M/60)))*2*math.pi)*A
My=math.sin((M/60)*2*math.pi)*B

print((math.sqrt((Hx-Mx)*(Hx-Mx)+(Hy-My)*(Hy-My))))

