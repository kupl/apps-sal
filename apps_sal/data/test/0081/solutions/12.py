
# //DEEPANSHU SAXENA(saxenad765)
# #include <bits/stdc++.h>
# #define ll long long
# #define array(x,n) (x,x+n)
# #define vector(v) (v.begin(),v.end())
# #define DEBUG(x) cout << '>' << #x << ':' << x << endl;
# #define VECTOR(v) cout << '>' << #v << ':' ; vector_out(v);
# #define fast ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
# #define ip(x) cin>>x
# #define op(x) cout<<x<<endl
# #define ops(x) cout<<x<<" "
# #define odd(x) (x&1)
# #define even(x) (!x&1)
# #define fbei(i,x,y,z) for(ll i=x;i<=y;i+=z)
# #define fbe(i,x,y) for(ll i=x;i<=y;i++)
# #define f(i,n) for(ll i=0;i<n;i++)
# #define pb push_back
# #define mp(x,y) make_pair(x,y)
# #define GCD(x,y) __gcd(x,y)
# using namespace std;
# //using codechef ide;
# //Deepanshu Saxena
# inline void filehandling()
# {
# 	#ifndef ONLINE_JUDGE
# 	freopen("input.txt", "r", stdin);
# 	freopen("output.txt", "w", stdout);
# 	#endif
# }
# vector<ll> vector_in(ll n)
# {
# 	vector<ll> v(n);
# 	for(ll i=0;i<n;i++)
# 	cin>>v[i];
# 	return v;
# }
# void vector_out(vector<ll> v)
# {
# 	for(ll i=0;i<v.size();i++)
# 	cout<<v[i]<<" ";
# 	cout<<endl;
# }
# ll vector_sum(vector<ll> v)
# {
# 	ll sum;
# 	for(ll i=0;i<v.size();i++)
# 	sum+=v[i];
# 	return sum;
# }
# int main()
# {
# 	fast
# 	filehandling();
a, b = list(map(int,input().split()))
def gcd(arg1,arg2):
	if arg1 == 0:
		return arg2
	if arg2 == 0:
		return arg1
	if arg2 > arg1:
		arg2,arg1 = arg1,arg2
	return gcd(arg1%arg2, arg2)
if a > b:
	a, b = b, a
k = b - a
array = []
i = 1
while i ** 2 <= k:
	if k % i == 0:
		array.append(i)
		array.append(k // i)
	i+= 1
gcdis = a * b / gcd(a,b)
z = 0
for d in array:
	z1 = a - (a % d) + d
	z2 = b - (b % d) + d
	if z1 * z2 // gcd(z1,z2) <= gcdis:
		if z1 * z2 // gcd(z1,z2) == gcdis:
			z = min(d-(a%d),z)
		else:
			gcdis = z1 * z2 // gcd(z1,z2)
			z = d-(a%d)
print(z)
# }


