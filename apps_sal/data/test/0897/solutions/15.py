from fractions import gcd;

def add(a,b,c,d):
	lcm =(b*d)//(gcd(b,d));
	aa = lcm//b;
	bb = lcm//d;
	#print("aa:",aa,"bb:",bb,"a:",a,"b:",b);
	aa = aa*a;
	bb = bb*c;
	#print("aa:",aa,"bb:",bb);
	cc = aa+bb;
	dd = gcd(lcm,cc);
	#print("cc:",cc);
	#print("lcm:",lcm);
	lcm = lcm//dd;
	cc = cc //dd;
	#print("cc:",cc);
	#print("lcm:",lcm);
	return cc,lcm;

def mul(a,b,c,d):
	aa = a*c;
	bb = b*d;
	dd = gcd(aa,bb);
	aa = aa//dd;
	bb = bb//dd;

	return aa,bb;

def eeuclid(a,b):
	q = a//b;
	r = a % b;

	if r == 1:
		return 1,-q;

	a,b = eeuclid(b,r);
	m = 1;
	n = -q;
	m = m * b;
	n = n * b;
	n = n + a;


	return m,n;

def mod_inverse(val,m):
	a,b = eeuclid(val,m);
	return a % m;

n,m = input().split();
n = int(n);
m = int(m);
mod_val = 1000000007;
arr1 = [];
arr2 = [];

arr1 = [int(x) for x in input().split()];
arr2 = [int(x) for x in input().split()];


num = [];
den = [];
prob = [];

for i in range(0,n):
	num.append(0);
	den.append(0);
	prob.append(0);
num.append(0);
den.append(1);
prob.append(0);

for i in range(n-1,-1,-1):
	if(arr1[i] != 0 and arr2[i] != 0):
		if(arr1[i] > arr2[i]):
			prob[i] = 1;
		elif(arr1[i] == arr2[i]):
			if(prob[i+1] == 0):
				prob[i] = 0;
			else:
				prob[i] = prob[i+1];
		elif(arr1[i] < arr2[i]):
			prob[i] = 0;
	
	elif(arr1[i] == 0 and arr2[i] != 0):
		num1 = m-arr2[i];
		inv1 = mod_inverse(m,mod_val);
		inv1 = inv1 % mod_val;
		qq = ((num1 % mod_val) * (inv1 % mod_val)) % mod_val;

		pp = inv1 * prob[i+1];

		prob[i] = (qq + pp) % mod_val;

	elif(arr1[i] != 0 and arr2[i] == 0):
		num1 = arr1[i]-1;
		inv1 = mod_inverse(m,mod_val);

		qq = ((num1 % mod_val) * (inv1 % mod_val)) % mod_val;

		pp = inv1 * prob[i+1];
		prob[i] = (qq + pp) % mod_val;
	else:
		aa = (m * (m-1))//2;
		aa = aa % mod_val;

		inv2 = mod_inverse(m*m,mod_val);
		inv1 = mod_inverse(m,mod_val);

		qq = (aa * inv2) % mod_val;
		pp = (inv1 * prob[i+1]) % mod_val;

		prob[i] = (pp + qq) % mod_val;

print((prob[0]));





