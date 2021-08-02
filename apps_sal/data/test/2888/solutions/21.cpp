#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define ull unsigned long long 
#define pb(e) push_back(e)
#define sv(a) sort(a.begin(),a.end())
#define sa(a,n) sort(a,a+n)
#define mp(a,b) make_pair(a,b)
#define vf first
#define vs second
const int inf = 0x3f3f3f3f;
int mod = 1000000007;
bool remender(ll a , ll b){return a%b;}
ll arr[5005];
map<pair<int,ll>,ll> m;
int n;
ll dig(ll x){
	ll res=0;
	while(x){
		res+=x%10;
		x/=10;
	}
	return res*res*res;
}

ll rec(int i , ll s){
	if(i==n)return 0;
	if(m[{i,s}]!=0)return m[{i,s}];
	return m[{i,s}]=max(rec(i+1,s+dig(s)),s*arr[i]+rec(i+1,s));
}

void solve(){
	ll s;
	cin>>n>>s;
	for(int i = 0; i < n; i++)cin>>arr[i];
	cout<<rec(0,s)<<"\n";
}

int main(){
ios_base::sync_with_stdio(false);
cin.tie(NULL);
	//int t;
	//cin >> t;
	//while(t--){
	solve();
	//}
	return 0;
}

