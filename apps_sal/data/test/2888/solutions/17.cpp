#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define inf 100000000000000
typedef long long ll;
#define mp make_pair
#define f first 
#define s second
int n;
ll en[5005];
ll power(ll x,ll y){
    ll res=1;
    while (y){
        if (y & 1){
            res=res*x; 
        }
        x=x*x;
        y=y>>1;
    }
    return res;
}
map<tuple<int,ll,ll>,ll> dp;
map<tuple<int,ll,ll>,bool> visited;
ll train(ll x){
    ll res=x;
    ll sum=0;
    while(x!=0){
        sum+=(x%10);
        x=x/10;
    }
    res+=power(sum,3);
    return res;
}
ll max_exp(int i,ll s,ll xp){
    if(i==n-1){
        return xp+s*en[i];
    }
    if(visited[{i,s,xp}]){
        return dp[{i,s,xp}];
    }
    dp[{i,s,xp}]=max(max_exp(i+1,train(s),xp),max_exp(i+1,s,xp+s*en[i]));
    visited[{i,s,xp}]=true;
    return dp[{i,s,xp}];
}
int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	cout.tie(NULL);
	ll s;
	cin>>n>>s;
	for(int i=0;i<n;i++){
	    cin>>en[i];
	}
	cout<<max_exp(0,s,0)<<"\n";
	return 0;
}
