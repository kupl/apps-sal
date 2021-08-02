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
ll dp[5005][5005];
int n;
ll dig(ll x){
	ll res=0;
	while(x){
		res+=x%10;
		x/=10;
	}
	return res*res*res;
}

ll rec(int i , ll s , int cnt){
	if(i==n)return 0;
	if(dp[i][cnt]!=-1)return dp[i][cnt];
	return dp[i][cnt]=max(rec(i+1,s+dig(s),cnt+1),s*arr[i]+rec(i+1,s,cnt));
}

void solve(){
	ll s;
	cin>>n>>s;
	for(int i = 0; i < n; i++)cin>>arr[i];
	memset(dp,-1,sizeof dp);
	cout<<rec(0,s,1)<<"\n";
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

